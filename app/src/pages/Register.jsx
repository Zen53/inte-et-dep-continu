import PersonForm from "../components/PersonForm"
import { Link } from 'react-router-dom';
import './Register.css'

/**
 * Register Component
 *
 * Wrapper page for PersonForm. Passes onSubmit callback to the form
 * and provides a link back to Home.
 *
 * @module Register
 * @component
 *
 * @param {Object} props
 * @param {function(Object): void} props.onSubmit - Callback called when a valid person is submitted
 *
 * @returns {JSX.Element}
 */
export default function Register({onSubmit}) {
    return (
        <div className="register-container">
            <PersonForm onSubmit={onSubmit}/>
            <Link to="/">
                <button data-cy="back-home" className="back-button">Retour à l'accueil</button>
            </Link>
        </div>
    )
}