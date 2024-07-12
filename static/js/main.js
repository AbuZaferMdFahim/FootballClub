function toggleBio(event) {
    event.preventDefault();
    var bioContent = document.getElementById('bio-content');
    var bioFullContent = document.getElementById('bio-full-content');
    var readMoreBtn = document.getElementById('read-more-btn');
    var showLessBtn = document.getElementById('show-less-btn');

    if (bioContent.style.display === 'none') {
        bioContent.style.display = 'block';
        bioFullContent.style.display = 'none';
        readMoreBtn.style.display = 'inline';
        showLessBtn.style.display = 'none';
    } else {
        bioContent.style.display = 'none';
        bioFullContent.style.display = 'block';
        readMoreBtn.style.display = 'none';
        showLessBtn.style.display = 'inline';
    }
}
document.getElementById('edit-profile').onclick = function() {
    document.getElementById('profile-info').style.display = 'none';
    document.getElementById('edit-profile-form').style.display = 'block';
};

document.getElementById('save-profile').onclick = function() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    const data = new FormData();
    data.append('first_name', document.getElementById('edit-first-name').value);
    data.append('last_name', document.getElementById('edit-last-name').value);
    data.append('email', document.getElementById('edit-email').value);
    data.append('bio', document.getElementById('edit-bio').value);
    data.append('mobile', document.getElementById('edit-mobile').value);

    fetch("{% url 'update_profile' %}", {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: data
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('first-name').textContent = document.getElementById('edit-first-name').value;
            document.getElementById('last-name').textContent = document.getElementById('edit-last-name').value;
            document.getElementById('email').textContent = document.getElementById('edit-email').value;
            document.getElementById('bio').textContent = document.getElementById('edit-bio').value;
            document.getElementById('mobile').textContent = document.getElementById('edit-mobile').value;

            document.getElementById('profile-info').style.display = 'block';
            document.getElementById('edit-profile-form').style.display = 'none';
        } else {
            alert('Error updating profile');
        }
    });
};
