import React from 'react';
import { Router, Route } from 'react-router';

import App from './App';
import RB from './PositionPages/RB';
import QB from './PositionPages/QB';
import WR from './PositionPages/WR';
import TE from './PositionPages/TE';

import DFS_home from './DFS/DFS_home';
// import NotFound from './components/NotFound';

const Routes = (props) => (
  <Router {...props}>
    <Route path="/" component={App} />
    <Route path="/RB" component={RB} />
    <Route path="/QB" component={QB} />
    <Route path="/WR" component={WR} />
    <Route path="/TE" component={TE} />
    <Route path="/DFS" component={DFS_home} />
  </Router>
);

export default Routes;
