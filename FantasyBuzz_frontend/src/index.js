import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';


import { browserHistory } from 'react-router';
import Routes from './routes';
import registerServiceWorker from './registerServiceWorker';
import 'bootstrap/dist/css/bootstrap.css';
import 'react-select/dist/react-select.css';


ReactDOM.render(
  <Routes history={browserHistory} />,
  document.getElementById('root')
);


registerServiceWorker();
