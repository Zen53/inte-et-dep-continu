import App from './App.jsx';
import PersonForm from './components/PersonForm.jsx';
import { validatePerson, validateAge, validateZipCode, validateCity, validateName, validateEmail } from './domain/validator.js';
import { errorMessages, getErrorMessage } from './utils/errorMessages.js';

export default App;
export { PersonForm, validatePerson, validateAge, validateZipCode, validateCity, validateName, validateEmail, errorMessages, getErrorMessage };
