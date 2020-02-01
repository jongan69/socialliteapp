import React from 'react';

import ReactDOM from 'react-dom';

import 'bootstrap/dist/css/bootstrap.css';

import './index.css';
import registerServiceWorker from './registerServiceWorker';

import App from './containers/App';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
