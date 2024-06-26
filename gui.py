import json
import os
import time
import threading
import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox
from webdesign import WebDesignAgent
from PIL import ImageTk, Image
from utils import cal_cost
import asyncio

class Application(tk.Tk):
    def __init__(self, agent=None):
        super().__init__()

        self.title("Web Design Agent")
        self.agent = agent
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        self.current_page = 0
        self.pages = []

        self.title_frame = tk.Frame(self)
        self.title_frame.grid(row=0, column=0, padx=10, pady=10)
        # Dropdown menu to select mode
        self.mode_var = tk.StringVar(value="Chat Mode")
        self.mode_options = ["Chat Mode", "Web Design Mode"]
        self.mode_menu = ttk.OptionMenu(self.title_frame, self.mode_var, self.mode_options[0], *self.mode_options, command=self.switch_mode)
        self.mode_menu.grid(row=0, column=1, padx=10, pady=10)
        self.mode_menu_label = tk.Label(self.title_frame, text="Select Mode:")
        self.mode_menu_label.grid(row=0, column=0, padx=10, pady=10)


        self.css_frame_var = tk.StringVar(value="Tailwind")
        self.agent.css_frame = "Tailwind"

        self.gen_img_var = tk.StringVar(value="Open")
        self.agent.gen_img = True

        self.model_options = ["gpt-4o","gpt-4-turbo-preview","gpt-3.5-turbo-0125"]
        self.model_var = tk.StringVar(value="gpt-4o")
        self.model_menu = ttk.OptionMenu(self.title_frame, self.model_var, self.model_options[0], *self.model_options,command=self.switch_model)
        self.model_menu.grid(row=0, column=3, padx=10, pady=10)
        self.model_menu_label = tk.Label(self.title_frame, text="Select Model:")
        self.model_menu_label.grid(row=0, column=2, padx=10, pady=10)

        self.is_animating = False

        self.canvas = tk.Canvas(self, width=int(screen_width * 0.8), height=int(screen_height*0.7))
        self.y_scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.x_scrollbar = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=self.x_scrollbar.set)
        self.canvas.configure(yscrollcommand=self.y_scrollbar.set)
        self.canvas.grid(row=1, column=0, padx=10, pady=10)
        self.y_scrollbar.grid(row=1, column=1, sticky="ns")
        self.x_scrollbar.grid(row=2, column=0, sticky="ew")

        # Chat mode widgets
        self.chat_widgets = self.create_chat_widgets()

        # Web design mode widgets
        self.web_design_widgets = self.create_web_design_widgets()
        # Show the initial mode
        self.switch_mode(self.mode_var.get())
        self.begin_time = time.time()
        with open("logs/token.json", "r") as f:
            tokens = json.load(f)
        self.begin_prompt_cost = tokens["gpt4o-0513"][0]
        self.begin_completion_cost = tokens["gpt4o-0513"][1]
        self.begin_dell_cost = tokens["dalle3"]
        self.total_cost = 0
        self.time_cost = 0
        self.img_ref = None     

    def create_chat_widgets(self):
        chat_widgets = {}

        chat_widgets['chat_history'] = scrolledtext.ScrolledText(self.scrollable_frame, wrap=tk.WORD, state='disabled', width=120, height=40)
        chat_widgets['input_area'] = tk.Text(self.scrollable_frame, height=3, width=120)
        chat_widgets['send_button'] = tk.Button(self.scrollable_frame, text="Send", command=self.send_message)
        return chat_widgets

    def create_web_design_widgets(self):
        web_design_widgets = {}
        web_design_widgets['input_frame'] = tk.Frame(self.scrollable_frame,width=700)
        web_design_widgets['output_text'] = scrolledtext.ScrolledText(self.scrollable_frame, wrap=tk.WORD, state='disabled', width=50, height=40)

        web_design_widgets['output_image_frame'] = tk.Frame(self.scrollable_frame, width=500,height=100)
        web_design_widgets["input_labels"] = []
        web_design_widgets["input_entries"] = []

        css_frame_options = ["Tailwind","Bootstrap","Materialize","Bulma","None"]
        self.css_frame_var = tk.StringVar(value="Tailwind")
        css_frame_menu = ttk.OptionMenu(web_design_widgets["input_frame"], self.css_frame_var, css_frame_options[0], *css_frame_options,command=self.on_css_frame_change)
        css_frame_menu.grid(row=0, column=1, padx=10, pady=10)
        css_frame_menu_label = tk.Label(web_design_widgets["input_frame"], text="CSS Framework:")
        css_frame_menu_label.grid(row=0, column=0, padx=10, pady=10)
        

        # Add multiple input fields to input_frame
        input_labels = ["save_file", "website_description", "website_img", "feedback","each refine times"]
        for i in range(1,6):
            label = tk.Label(web_design_widgets['input_frame'], text=input_labels[i-1])
            entry = tk.Entry(web_design_widgets['input_frame'])
            label.grid(row=i, column=0, padx=10, pady=5)
            entry.grid(row=i, column=1, padx=10, pady=5)
            web_design_widgets["input_labels"].append(label)
            web_design_widgets["input_entries"].append(entry)

        gen_img_options = [ "Open","Close"]
        gen_img_var = tk.StringVar(value="Open")
        self.gen_img_var = gen_img_var
        gen_img_menu = ttk.OptionMenu(web_design_widgets["input_frame"], gen_img_var, gen_img_options[0], *gen_img_options,command=self.change_gen_img)
        gen_img_menu.grid(row=6, column=1, padx=10, pady=10)
        gen_img_menu_label = tk.Label(web_design_widgets["input_frame"], text="Gen IMG:")
        gen_img_menu_label.grid(row=6, column=0, padx=10, pady=10)
        

        # Animation Label
        label = tk.Label(web_design_widgets["input_frame"], text="🤖 Status: ")
        label.grid(row=7, column=0, padx=10, pady=10)
        self.animation_label = tk.Label(web_design_widgets["input_frame"], text="💡 idle")
        self.animation_label.grid(row=7, column=1, columnspan=2, padx=10, pady=10)
        self.animation_idx = 0

        # cost label
        label = tk.Label(web_design_widgets["input_frame"], text="💰 Total Token Cost: ")
        label.grid(row=8, column=0, padx=10, pady=10)
        self.token_cost_label = tk.Label(web_design_widgets["input_frame"], wraplength=200,text="💰 0 $")
        self.token_cost_label.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

        label = tk.Label(web_design_widgets["input_frame"], text="💰 Total IMG Cost: ")
        label.grid(row=9, column=0, padx=10, pady=10)
        self.token_img_label = tk.Label(web_design_widgets["input_frame"], wraplength=200,text="💰 0 $")
        self.token_img_label.grid(row=9, column=1, columnspan=2, padx=10, pady=10)        


        label = tk.Label(web_design_widgets["input_frame"], text="⏱️ Time Cost: ")
        label.grid(row=10, column=0, padx=10, pady=10)
        self.time_label = tk.Label(web_design_widgets["input_frame"], wraplength=200,text="⏱️ 0 s")
        self.time_label.grid(row=10, column=1, columnspan=2, padx=10, pady=10)

        plan_button = tk.Button(self.scrollable_frame, text="Plan", command=self.plan)
        auto_gen_button = tk.Button(self.scrollable_frame, text="Auto Generate", command=self.auto_gen_website)
        create_button = tk.Button(self.scrollable_frame, text="Create Website", command=self.create_website)
        refine_button = tk.Button(self.scrollable_frame, text="Refine Website", command=self.refine_website)

        delete_page_button = tk.Button(self.scrollable_frame, text="Delete Page", command=self.delete_page)
        add_page_button = tk.Button(self.scrollable_frame, text="Add Page", command=self.add_page)
        complete_page_button = tk.Button(self.scrollable_frame, text="Complete Page", command=self.complete_page)
        refine_page_button = tk.Button(self.scrollable_frame, text="Refine Page", command=self.refine_page)

        web_design_widgets["plan_button"] = plan_button
        web_design_widgets["auto_gen_button"] = auto_gen_button

        web_design_widgets["create_button"] = create_button
        web_design_widgets["refine_button"] = refine_button

        web_design_widgets["delete_page_button"] = delete_page_button
        web_design_widgets["add_page_button"] = add_page_button
        web_design_widgets["complete_page_button"] = complete_page_button
        web_design_widgets["refine_page_button"] = refine_page_button

        return web_design_widgets


    def on_css_frame_change(self, css_frame):
        if css_frame == "None":
            self.agent.css_frame = None
        else:
            self.agent.css_frame = css_frame
        print(f"Change CSS Frame to: {css_frame}")

    def switch_model(self,model):
        self.agent.model = model
        print(f"Switched to {model}")

    def switch_mode(self, mode):
        self.clear_widgets()
        if mode == "Chat Mode":
            self.model_options = ["gpt-4o","gpt-4-turbo-preview","gpt-3.5-turbo-0125"]
            self.model_menu.set_menu(self.model_options[0],*self.model_options)
            self.display_chat_mode()
        elif mode == "Web Design Mode":
            self.model_options = ["gpt-4o"]
            self.model_menu.set_menu(self.model_options[0],*self.model_options)
            self.display_web_design_mode()
        print(f"Switched to {mode}")
    
    def clear_widgets(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.grid_forget()
    
    def display_chat_mode(self):
        self.chat_widgets['chat_history'].grid(row=1, column=0,  padx=10, pady=10)
        self.chat_widgets['input_area'].grid(row=2, column=0, padx=10, pady=10)
        self.chat_widgets['send_button'].grid(row=2, column=1, padx=10, pady=10)
    
    def display_web_design_mode(self):
        self.web_design_widgets['input_frame'].grid(row=1, column=0, padx=10, pady=10)
        self.web_design_widgets['plan_button'].grid(row=2, column=0, padx=10, pady=10)
        self.web_design_widgets['auto_gen_button'].grid(row=3, column=0, padx=10, pady=10)

        self.web_design_widgets['output_text'].grid(row=1, column=1, padx=10, pady=10)
        self.web_design_widgets['delete_page_button'].grid(row=2, column=1, padx=10, pady=10)
        self.web_design_widgets['add_page_button'].grid(row=3, column=1, padx=10, pady=10)
        self.web_design_widgets['complete_page_button'].grid(row=4, column=1, padx=10, pady=10)
        self.web_design_widgets['refine_page_button'].grid(row=5, column=1, padx=10, pady=10)

        self.web_design_widgets['output_image_frame'].grid(row=1, column=2, padx=10, pady=10)

        self.web_design_widgets['create_button'].grid(row=3, column=2, padx=10, pady=10)
        self.web_design_widgets['refine_button'].grid(row=4, column=2, padx=10, pady=10)

    
    def send_message(self):
        message = self.chat_widgets['input_area'].get("1.0", tk.END).strip()
        if message:
            self.update_chat("You", message)
            self.chat_widgets['input_area'].delete("1.0", tk.END)
            self.chat_widgets['input_area'].insert(tk.END, "Thinking now")
            response = self.agent.chat(message)
            self.chat_widgets['input_area'].delete("1.0", tk.END)
            self.update_chat("Bot", response)
    
    def update_chat(self, sender, message):
        self.chat_widgets['chat_history'].config(state='normal')
        self.chat_widgets['chat_history'].insert(tk.END, f"{sender}: {message}\n")
        self.chat_widgets['chat_history'].config(state='disabled')
        self.chat_widgets['chat_history'].see(tk.END)
    
    def plan(self):
        if self.is_animating:
            messagebox.showerror("Error", "Please wait for the current operation to finish")
            return
        def long_operation():
            self.pages = self.agent.plan()
            self.is_animating = False
            self.current_page = 0
            self.display_table_page()
            self.update_cost()

        for widget in self.web_design_widgets['output_image_frame'].winfo_children():
            widget.destroy()
        for widget in self.web_design_widgets['output_text'].winfo_children():
            widget.destroy()

        if not self.agent:
            messagebox.showerror("Error", "Please initialize the agent first")
            return

        save_file = self.web_design_widgets["input_entries"][0].get()
        self.agent.change_save_file(save_file)
        website_description = self.web_design_widgets["input_entries"][1].get()
        website_img = self.web_design_widgets["input_entries"][2].get()
        if not website_description and not os.path.exists(website_img):
            try:
                self.agent.driver.get_screenshot(website_img,"target_website.png",False)
            except:
                messagebox.showerror("Error", "Please upload the website image or input the website description")
                return

        self.agent.publish_task(img=website_img, text=website_description)

        animation_sequence = ["🤔💭 Planning now", "🧐💭 Planning now.", "😅💭 Planning now..", "🤯💭 Planning now..."]
        self.is_animating = True
        self.begin_time = time.time()
        threading.Thread(target=self.animate, args=(animation_sequence,)).start()
        threading.Thread(target=long_operation).start()
    

    def change_gen_img(self,gen_img):
        if gen_img == "Open":
            self.agent.gen_img = True
        else:
            self.agent.gen_img = False
        print(f"Change Gen IMG to: {gen_img}")

    
    def display_table_page(self):
        table_frame = self.web_design_widgets["output_text"]
        for widget in table_frame.winfo_children():
            widget.destroy()
        
        table_frame.config(state='disabled', wrap=tk.WORD, width=50, height=50)
        if self.pages:
            item = self.pages[self.current_page]
            cnt = 0
            for i, (key, value) in enumerate(item.items()):
                tk.Label(table_frame, text=key).grid(row=i, column=0, sticky='e')
                text_frame = tk.Frame(table_frame)
                text_frame.grid(row=i, column=1, sticky='w')
                if key in ["is_main_page","html_name","css_name"]:
                    text_widget = tk.Text(text_frame, wrap=tk.WORD, height=1, width=30)
                elif key == "relationship":
                    text_widget = tk.Text(text_frame, wrap=tk.WORD, height=15, width=30)
                else:
                    text_widget = tk.Text(text_frame, wrap=tk.WORD, height=5, width=30)
                text_widget.insert(tk.END, value)
                text_widget.pack(side=tk.LEFT, expand=True, fill='both')
                scrollbar = tk.Scrollbar(text_frame, command=text_widget.yview)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                text_widget.config(yscrollcommand=scrollbar.set)
                text_widget.bind("<FocusOut>", lambda e, k=key, idx=self.current_page: self.save_value(e, k, idx))
                cnt = i
            
            canvas = tk.Canvas(table_frame, width=500, height=80)
            canvas.grid(row=cnt+1, column=0, columnspan=2)
            scrollbar = tk.Scrollbar(table_frame, command=canvas.yview)
            scrollbar.grid(row=cnt+1, column=2, sticky='ns')
            canvas.config(yscrollcommand=scrollbar.set)
            self.inner_frame = tk.Frame(canvas)
            self.inner_frame_id = canvas.create_window((0, 0), window=self.inner_frame, anchor='nw')
            self.create_blocks(self.inner_frame)
            self.inner_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
            # Bind resizing events
            self.block_canvas = canvas
            self.inner_frame.bind('<Configure>', self.on_frame_resize)

            html_name = item["html_name"]
            html_path = os.path.join(self.agent.save_file, html_name)
            page_name = html_name.split(".")[0]
            page_img_path = os.path.join(self.agent.save_file, f"{page_name}.png")
            if html_name and os.path.exists(html_path):
                if not os.path.exists(page_img_path):
                    self.agent.webserver.get_screenshot(html_path, page_img_path)
                self.update_ui_after_refine_website()


        table_frame.grid(row=1, column=1, padx=10, pady=10)
    
    def create_blocks(self, frame):
        self.buttons = []  # Keep track of rectangle ID
        block_width = 5
        blocks_per_row =  6
        page_list = self.pages
        for idx, value in enumerate(page_list):
            html_name = value["html_name"]
            html_path = os.path.join(self.agent.save_file, html_name)
            color = "green" if os.path.exists(html_path) else "gray"
            row = idx // blocks_per_row
            col = idx % blocks_per_row
            page_name = html_name.split(".")[0]
            button = tk.Button(frame, text=page_name, bg=color, width=block_width, height=2,
                               command=lambda idx=idx: self.on_block_click(idx),font=("Arial", 10))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

    def on_frame_resize(self, event):
        canvas_width = event.width
        self.nametowidget(self.block_canvas).itemconfig(self.inner_frame_id, width=canvas_width)
        self.nametowidget(self.block_canvas).config(scrollregion=self.nametowidget(self.block_canvas).bbox("all"))


    def on_block_click(self, idx):
        self.current_page = idx
        self.display_table_page()


    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.display_table_page()
    
    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.display_table_page()
    
    def delete_page(self):
        if self.pages:
            current_page = self.pages[self.current_page]
            html_name = current_page["html_name"]
            for i,page in enumerate(self.pages):
                if isinstance(page["relationship"], dict):
                    for j,button in enumerate(page["relationship"]["buttons"]):
                        if "jump_page" in button and button["jump_page"] == html_name:
                            self.pages[i]["relationship"]["buttons"].pop(j)
                    for j,link in enumerate(page["relationship"]["links"]):
                        if "jump_page" in link and link["jump_page"] == html_name:
                            self.pages[i]["relationship"]["links"].pop(j)
            self.pages.pop(self.current_page)
            if self.current_page >= len(self.pages):
                self.current_page = len(self.pages) - 1
            self.display_table_page()

    def refine_page(self):
        if self.is_animating:
            messagebox.showerror("Error", "Please wait for the current operation to finish")
            return
        if self.pages:
            animation_sequence = ["🤔💭 Refine now", "🧐💭 Refine now.", "😅💭 Refine now..", "🤯💭 Refine now..."]
            self.is_animating = True
            threading.Thread(target=self.animate, args=(animation_sequence,)).start()
            def long_operation():
                page = self.pages[self.current_page]
                html_name = page["html_name"]
                html_path = os.path.join(self.agent.save_file, html_name)
                if not os.path.exists(html_path):
                    messagebox.showerror("Error", "Please create the website first")
                    return
                feedback = self.web_design_widgets["input_entries"][3].get()
                self.pages[self.current_page] = self.agent.refine_page(page,feedback)
                with open(os.path.join(self.agent.save_file, "pages.json"), "w",encoding='utf-8') as f:
                    json.dump(self.pages, f)
                self.is_animating = False
                self.display_table_page()
                self.update_cost()
            self.begin_time = time.time()
            threading.Thread(target=long_operation).start()

    def complete_page(self):
        if self.is_animating:
            messagebox.showerror("Error", "Please wait for the current operation to finish")
            return
        self.is_animating = True
        animation_sequence = ["🤔💭 Completing now", "🧐💭 Completing now.", "😅💭 Completing now..", "🤯💭 Completing now..."]
        threading.Thread(target=self.animate, args=(animation_sequence,)).start()
        def long_operation():
            self.pages = self.agent.complete_page(self.pages, self.current_page)
            with open(os.path.join(self.agent.save_file, "pages.json"), "w",encoding='utf-8') as f:
                json.dump(self.pages, f)
            self.is_animating = False
            self.display_table_page()
            self.update_cost()
        self.begin_time = time.time()
        threading.Thread(target=long_operation).start()

    def add_page(self):
        page_template = {}
        for key in self.pages[0].keys():
            page_template[key] = ""
        self.pages.append(page_template)
        self.current_page = len(self.pages) - 1
        self.display_table_page()
    
    def save_value(self, event, key, idx):
        text_widget = event.widget
        text_widget.config(state=tk.NORMAL)
        value = text_widget.get("1.0", tk.END).strip()
        text_widget.config(state=tk.DISABLED)
        self.pages[idx][key] = value
        save_file = self.web_design_widgets["input_entries"][0].get()
        pages_path = os.path.join(save_file, "pages.json")
        with open(pages_path, "w",encoding='utf-8') as f:
            json.dump(self.pages, f)
    
    def update_cost(self):
        with open("logs/token.json", "r") as f:
            tokens = json.load(f)
        current_prompt_cost = tokens["gpt4o-0513"][0]
        current_completion_cost = tokens["gpt4o-0513"][1]
        current_del_cost = tokens["dalle3"]
        total_prompt_cost = current_prompt_cost - self.begin_prompt_cost
        total_completion_cost = current_completion_cost - self.begin_completion_cost
        self.total_cost = cal_cost(total_prompt_cost, total_completion_cost)
        self.time_cost += time.time() - self.begin_time
        self.token_cost_label.config(text=f"💰 {self.total_cost} $")
        self.token_img_label.config(text=f"💰 {(current_del_cost - self.begin_dell_cost) * 4 / 100} $")
        self.time_label.config(text=f"⏱️ {self.time_cost} s")
    
    def create_website(self):
        animation_sequence = ["🤔💭 Creating now", "🧐💭 Creating now.", "😅💭 Creating now..", "🤯💭 Creating now..."]
        if self.is_animating:
            messagebox.showerror("Error", "Please wait for the current operation to finish")
            return
        
        website_description = self.web_design_widgets["input_entries"][1].get()
        website_img = self.web_design_widgets["input_entries"][2].get()
        self.agent.task["text"] = website_description
        self.agent.task["img"] = website_img

        self.is_animating = True
        threading.Thread(target=self.animate, args=(animation_sequence,)).start()
        def long_operation():
            if not self.pages:
                messagebox.showerror("Error", "Please plan the website first")
                return
            page = self.pages[self.current_page]
            self.agent.write_original_website(page)
            self.after(0, self.update_ui_after_refine_website)
            self.is_animating = False
            self.update_cost()

        self.begin_time = time.time()
        threading.Thread(target=long_operation).start()
    
    def refine_website(self):
        if self.is_animating:
            messagebox.showerror("Error", "Please wait for the current operation to finish")
            return
        animation_sequence = ["🤔💭 Refine now", "🧐💭 Refine now.", "😅💭 Refine now..", "🤯💭 Refine now..."]
        self.is_animating = True
        threading.Thread(target=self.animate, args=(animation_sequence,)).start()
        website_description = self.web_design_widgets["input_entries"][1].get()
        website_img = self.web_design_widgets["input_entries"][2].get()
        self.agent.task["text"] = website_description
        self.agent.task["img"] = website_img

        def long_operation():
            self.agent.user_feedback = self.web_design_widgets["input_entries"][3].get()
            page = self.pages[self.current_page]
            html_name = page["html_name"]
            html_path = os.path.join(self.agent.save_file, html_name)
            if not os.path.exists(html_path):
                messagebox.showerror("Error", "Please create the website first")
                return
            self.agent.refine(page)
            
            # Update UI on the main thread
            self.after(0, self.update_ui_after_refine_website)
            self.is_animating = False
            self.update_cost()
        self.begin_time = time.time()
        threading.Thread(target=long_operation).start()

    def update_ui_after_refine_website(self):
        page = self.pages[self.current_page]
        html_name = page["html_name"]
        for widget in self.web_design_widgets['output_image_frame'].winfo_children():
            widget.destroy()

        if os.path.exists(os.path.join(self.agent.save_file, html_name)):
            page_name = html_name.split(".")[0]
            page_img_path = os.path.join(self.agent.save_file, f"{page_name}.png")
            img = Image.open(page_img_path)
            if img.size[0] > 600:
                width,height = img.size
                img = img.resize((600, int(600/width*height)))
            img = ImageTk.PhotoImage(img)
            canvas = tk.Canvas(self.web_design_widgets['output_image_frame'], width=600, height=600)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            v_scrollbar = tk.Scrollbar(self.web_design_widgets['output_image_frame'], orient=tk.VERTICAL, command=canvas.yview)
            x_scrollbar = tk.Scrollbar(self.web_design_widgets['output_image_frame'], orient=tk.HORIZONTAL, command=canvas.xview)
            v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
            canvas.configure(yscrollcommand=v_scrollbar.set)
            canvas.configure(xscrollcommand=x_scrollbar.set)
            image_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=image_frame, anchor="nw")
            img_label = tk.Label(image_frame, image=img)
            img_label.image = img
            img_label.pack()
            image_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            # Bind resize event to update scrollregion
            def on_frame_resize(event):
                canvas.config(scrollregion=canvas.bbox("all"))

            image_frame.bind("<Configure>", on_frame_resize)            
            self.img_ref = img


    def auto_gen_website(self):
        if self.is_animating:
            messagebox.showerror("Error", "Please wait for the current operation to finish")
            return
        self.is_animating = True
        animation_sequence = ["🤔💭 Generating now", "🧐💭 Generating now.", "😅💭 Generating now..", "🤯💭 Generating now..."]
        self.refine_times = int(self.web_design_widgets["input_entries"][4].get()) if self.web_design_widgets["input_entries"][4].get() else 3
        self.agent.refine_times = self.refine_times
        web_description = self.web_design_widgets["input_entries"][1].get()
        web_img = self.web_design_widgets["input_entries"][2].get()
        self.agent.task["text"] = web_description
        self.agent.task["img"] = web_img
        
        threading.Thread(target=self.animate, args=(animation_sequence,)).start()
        def long_operation():
            self.begin_time = time.time()
            if not self.pages:
                self.pages = self.agent.plan()
            self.update_cost()
            need_create_pages = []
            for page in self.pages:
                html_name = page["html_name"]
                html_path = os.path.join(self.agent.save_file, html_name)
                if not os.path.exists(html_path) and page["description"]:
                    need_create_pages.append(page)
            
            asyncio.run(self.agent.deal_task_async(need_create_pages))
            self.update_cost()
            self.is_animating = False
        threading.Thread(target=long_operation).start()


    def animate(self,animation_sequence):
        if self.is_animating:
            self.animation_label.config(text=animation_sequence[self.animation_idx])
            self.animation_idx = (self.animation_idx + 1) % len(animation_sequence)
            self.after(300, lambda: self.animate(animation_sequence))
        else:
            self.animation_label.config(text="💡 idle")


if __name__ == "__main__":
    agent = WebDesignAgent()
    app = Application(agent=agent)
    app.mainloop()