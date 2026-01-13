


function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');

    sidebar.classList.toggle('open');
    content.classList.toggle('shifted');
  }

  
  function copyApiKey(user) {
    // Get the target element by ID
    var targetElement = document.getElementById(user);     
    // Create a temporary textarea element
    var tempTextArea = document.createElement('textarea');
    // Set the textarea value to the text content of the target element
    tempTextArea.value = targetElement.textContent;
    // Append the textarea to the document body
    document.body.appendChild(tempTextArea);
    // Select the text in the textarea
    tempTextArea.select();
    // Copy the selected text to the clipboard
    document.execCommand('copy');
    // Remove the temporary textarea
    document.body.removeChild(tempTextArea);
    // Optionally, display a notification or perform other actions
    swal("Copied!", "Copied to clipboard", "success");
  }