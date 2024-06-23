// about.js
document.addEventListener('DOMContentLoaded', function() {
    // Sample team members
    const teamMembers = [
        { imgSrc: "team1.jpg", description: 'Team member 1 - CEO' },
        { imgSrc: "team2.jpg", description: 'Team member 2 - CTO' },
        { imgSrc: "team3.jpg", description: 'Team member 3 - CFO' }
    ];

    const teamContainer = document.getElementById('team-members');
    teamMembers.forEach(member => {
        const imgContainer = document.createElement('div');
        const img = document.createElement('img');
        img.src = member.imgSrc;
        img.alt = member.description;
        img.setAttribute('description', member.description);
        imgContainer.appendChild(img);

        const desc = document.createElement('div');
        desc.classList.add('description');
        desc.innerText = member.description;
        imgContainer.appendChild(desc);

        teamContainer.appendChild(imgContainer);
    });

    // Interactive timeline
    const timelineData = [
        { year: "2020", event: "Platform Launched" },
        { year: "2021", event: "First 1000 Users" },
        { year: "2022", event: "Expansion to Europe" }
    ];

    const timelineContainer = document.getElementById('timeline');
    timelineData.forEach(item => {
        const div = document.createElement('div');
        div.innerHTML = `<strong>${item.year}</strong>: ${item.event}`;
        div.style.margin = "10px";
        timelineContainer.appendChild(div);
    });

    // Customer Testimonials
    const testimonials = [
        { text: "This platform is amazing!", author: "John Doe" },
        { text: "I love using this platform.", author: "Jane Smith" },
        { text: "Highly recommend to everyone.", author: "Alice Johnson" }
    ];

    const testimonialContainer = document.getElementById('testimonial-container');
    testimonials.forEach(testimonial => {
        const div = document.createElement('div');
        div.innerHTML = `<p>${testimonial.text}</p><p><strong>- ${testimonial.author}</strong></p>`;
        testimonialContainer.appendChild(div);
    });

    // FAQ Section
    const faqData = [
        { question: "How do I sign up?", answer: "You can sign up by clicking the 'Sign Up' button on the home page." },
        { question: "What features are available?", answer: "We offer a range of features including..." }
    ];

    const faqContainer = document.getElementById('faq-container');
    faqData.forEach(faq => {
        const question = document.createElement('div');
        question.innerHTML = `<strong>${faq.question}</strong>`;
        question.style.cursor = "pointer";
        question.style.margin = "10px 0";
        const answer = document.createElement('div');
        answer.innerHTML = `${faq.answer}`;
        answer.style.display = "none";
        answer.style.margin = "5px 0";

        question.addEventListener('click', () => {
            answer.style.display = answer.style.display === "none" ? "block" : "none";
        });

        faqContainer.appendChild(question);
        faqContainer.appendChild(answer);
    });

    // Tooltips for team members
    const images = document.querySelectorAll('#team-members img');
    images.forEach(img => {
        img.addEventListener('mouseenter', (e) => {
            const tooltip = document.createElement('div');
            tooltip.classList.add('tooltip');
            tooltip.innerHTML = e.target.getAttribute('description');
            tooltip.style.position = 'absolute';
            tooltip.style.backgroundColor = '#333';
            tooltip.style.color = '#fff';
            tooltip.style.padding = '5px';
            tooltip.style.borderRadius = '5px';
            tooltip.style.top = `${e.pageY}px`;
            tooltip.style.left = `${e.pageX}px`;
            document.body.appendChild(tooltip);
            e.target.tooltip = tooltip;
        });

        img.addEventListener('mouseleave', (e) => {
            document.body.removeChild(e.target.tooltip);
        });
    });

    // Enhance testimonials carousel
    let currentIndex = 0;
    const testimonialItems = document.querySelectorAll('.carousel div');
    const showTestimonial = (index) => {
        testimonialItems.forEach((item, i) => {
            item.style.display = i === index ? 'block' : 'none';
        });
    };
    showTestimonial(currentIndex);

    const nextTestimonial = () => {
        currentIndex = (currentIndex + 1) % testimonialItems.length;
        showTestimonial(currentIndex);
    };

    const prevTestimonial = () => {
        currentIndex = (currentIndex - 1 + testimonialItems.length) % testimonialItems.length;
        showTestimonial(currentIndex);
    };

    document.getElementById('next').addEventListener('click', nextTestimonial);
    document.getElementById('prev').addEventListener('click', prevTestimonial);

    setInterval(nextTestimonial, 3000);
});