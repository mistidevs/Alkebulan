// Select DOM Elements
const loginForm = document.querySelector('#loginForm');
const usernameInput = document.getElementById('userNameInput');
const fullNameInput = document.getElementById('fullNameInput');
const passwordInput = document.getElementById('passwordInput');
const phoneNumberInput = document.getElementById('phoneNumberInput');
const emailAddressInput = document.getElementById('emailAddressInput');

function validate() {
    // Check if any of the fields are empty
    const isAnyEmpty = [...arguments].some(elem => elem === '');
    return !isAnyEmpty;
};

async function postData(url = 'http://127.0.0.1:5000/api/v1/consumers', data = {}) {
  try {
      const response = await fetch(url, {
          method: 'POST', // Set the method to POST
          mode: 'cors',
          cache: 'no-cache',
          credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/json'
          },
          redirect: 'follow',
          referrerPolicy: 'no-referrer',
          body: JSON.stringify({data}),
      });
      console.log("Successful");
      alert("Your details have been submitted successfully!");
  } catch (error) {
      console.warn(`Error while submitting data:\n${error}`);
  };
};

loginForm.addEventListener('submit', async e => {
    e.preventDefault();
    
    const validatedFields = validate(usernameInput.value, fullNameInput.value, passwordInput.value, phoneNumberInput.value, emailAddressInput.value);
    
    if (!validatedFields) {
        alert("Please fill up all the necessary information.");
        return false;
    };
    
    const jsonBody = {
        "username": usernameInput.value,
        "full_name": fullNameInput.value,
        "password": passwordInput.value,
        "phone_number": phoneNumberInput.value,
        "email_address": emailAddressInput.value
    };
    
    await postData('http://127.0.0.1:5000/api/v1/consumers', jsonBody);
});