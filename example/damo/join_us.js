document.addEventListener('DOMContentLoaded', function() {
    const applyJobBtn = document.getElementById('apply-job-btn');
    const jobApplicationModal = document.getElementById('job-application-modal');
    const registerMemberBtn = document.getElementById('register-member-btn');
    const membershipRegistrationModal = document.getElementById('membership-registration-modal');

    applyJobBtn.addEventListener('click', function() {
        jobApplicationModal.style.display = 'block';
    });

    registerMemberBtn.addEventListener('click', function() {
        membershipRegistrationModal.style.display = 'block';
    });

    document.querySelectorAll('.close').forEach(closeBtn => {
        closeBtn.addEventListener('click', function() {
            jobApplicationModal.style.display = 'none';
            membershipRegistrationModal.style.display = 'none';
        });
    });

    window.addEventListener('click', function(event) {
        if (event.target == jobApplicationModal) {
            jobApplicationModal.style.display = 'none';
        }
        if (event.target == membershipRegistrationModal) {
            membershipRegistrationModal.style.display = 'none';
        }
    });

    document.getElementById('job-application-form').addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Job application submitted!');
        jobApplicationModal.style.display = 'none';
    });

    document.getElementById('membership-registration-form').addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Membership registration submitted!');
        membershipRegistrationModal.style.display = 'none';
    });
});