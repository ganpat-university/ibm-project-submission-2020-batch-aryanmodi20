// Get the form elements
const signInForm = document.querySelector('.sign-in-form');
const signUpForm = document.querySelector('.sign-up-form');
const usernameInput = signInForm.querySelector('input[placeholder="Username"]');
const passwordInput = signInForm.querySelector('input[placeholder="Password"]');
const signUpUsernameInput = signUpForm.querySelector('input[name="username"]');
const signUpEmailInput = signUpForm.querySelector('input[name="email"]');
const signUpPasswordInput = signUpForm.querySelector('input[name="password"]');

// Add event listener for login form submission
signInForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior
  clearErrors(); // Clear previous error messages

  // Validate username
  if (usernameInput.value.trim() === '') {
    displayError(usernameInput, 'Username is required');
  }

  // Validate password
  if (passwordInput.value.trim() === '') {
    displayError(passwordInput, 'Password is required');
  }

  // If both fields are valid, submit the form
  if (usernameInput.value.trim() !== '' && passwordInput.value.trim() !== '') {
    signInForm.submit(); // Submit the form
  }
});

// Add event listener for sign-up form submission
signUpForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent default form submission behavior
  clearErrors(); // Clear previous error messages

  // Validate username
  if (signUpUsernameInput.value.trim() === '') {
    displayError(signUpUsernameInput, 'Username is required');
  }

  // Validate email
  if (signUpEmailInput.value.trim() === '') {
    displayError(signUpEmailInput, 'Email is required');
  }

  // Validate password
  if (signUpPasswordInput.value.trim() === '') {
    displayError(signUpPasswordInput, 'Password is required');
  } else if (signUpPasswordInput.value.trim().length < 8) {
    displayError(signUpPasswordInput, 'Password must be at least 8 characters long');
  }

  // If all fields are valid, submit the form
  if (
    signUpUsernameInput.value.trim() !== '' &&
    signUpEmailInput.value.trim() !== '' &&
    signUpPasswordInput.value.trim() !== ''
  ) {
    signUpForm.submit(); // Submit the form
  }
});

// Function to display error messages
function displayError(inputElement, errorMessage) {
  const errorElement = document.createElement('div');
  errorElement.textContent = errorMessage;
  errorElement.style.color = 'red';
  inputElement.after(errorElement);
}

// Function to clear previous error messages
function clearErrors() {
  const errorMessages = document.querySelectorAll('.input-error');
  errorMessages.forEach(errorMessage => {
    errorMessage.remove();
  });
}

document.addEventListener('DOMContentLoaded', function() {
  const sign_in_btn = document.querySelector('#sign-in-btn');
  const sign_up_btn = document.querySelector('#sign-up-btn');
  const container = document.querySelector('.container');

  if (sign_up_btn && sign_in_btn && container) {
    sign_up_btn.addEventListener('click', () => {
      container.classList.add('sign-up-mode');
    });

    sign_in_btn.addEventListener('click', () => {
      container.classList.remove('sign-up-mode');
    });
  }
});