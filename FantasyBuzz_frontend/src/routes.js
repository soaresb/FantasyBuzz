import React from 'react';
import { Router, Route } from 'react-router';

import App from './App';
import RB from './PositionPages/RB';
import QB from './PositionPages/QB';
import WR from './PositionPages/WR';
import TE from './PositionPages/TE';
import DFS_home from './DFS/DFS_home';
import DFS_QB from './DFS/DFS_QB';
import DFS_RB from './DFS/DFS_RB';
import { browserHistory } from 'react-router';
// import NotFound from './components/NotFound';

const Routes = (props) => (
  <Router history={browserHistory} {...props}>
    <Route path="/" component={App} />
      <Route path="/RB" component={RB} />
      <Route path="/QB" component={QB} />
      <Route path="/WR" component={WR} />
      <Route path="/TE" component={TE} />
      <Route path="/DFS" component={DFS_home} />
      <Route path="/DFS/QB" component={DFS_QB} />
      <Route path="/DFS/RB" component={DFS_RB} />

  </Router>
);

export default Routes;
