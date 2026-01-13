function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');

    sidebar.classList.toggle('open');
    content.classList.toggle('shifted');
  }


  function moveNews() {
    const element = document.getElementById('section1');
  
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }


function moveRegion() {
    const element = document.getElementById('section2');
  
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }
  
  function movegettingStarted() {
    const element = document.getElementById('gettingStarted');
  
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }


  function moveSports() {
    const element = document.getElementById('section3');
  
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }


  function moveEntertainment() {
    const element = document.getElementById('section4');
  
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }

  
  function moveAssets() {
    const element = document.getElementById('section5');
  
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }

  function moveWorld() {
    const element = document.getElementById('section6');
  
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }

  function copyText(user) {
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