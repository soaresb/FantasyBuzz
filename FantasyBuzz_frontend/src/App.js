import React, { Component } from 'react';
import './App.css';
import $ from 'jquery';
import Player from './Components/Player';
import { Button } from 'reactstrap';
import BuzzNav from './Components/BuzzNav';
import { Jumbotron, Container } from 'reactstrap';
var jumboStyle = {
  margin: '0',

};
class App extends Component {
  constructor(){
    super();
    this.state = {
      players:[]
    }
  }
  getStats(){
    $.ajax({
      url: 'https://lolstats-backend.herokuapp.com/ffb/all',
      dataType:'json',
      cache:false,
      success: function(data){
        this.setState({players: data.cursor});

      }.bind(this),
      error: function(xhr, status, err){
        console.log(err);
      }
    });
  }
  componentWillMount(){
    this.getStats();
  }

  componentDidMount(){
    this.getStats();
  }
  render() {
    return (
      <div className="App">
        <BuzzNav />
        <div>
          <Jumbotron fluid style={jumboStyle} >
            <Container fluid>
              <h1 className="display-3">FantasyBuzz</h1>
              <p className="lead">
                FantasyBuzz searches for player mentions in articles from the top fantasy analysts including analysts from The Fantasy Footballers,
                RotoWorld, FantasyPros, Yahoo Fantasy, etc.
              </p>
            </Container>
          </Jumbotron>
        </div>
        <Player player={this.state.players} />

        <Button color="danger">Danger!</Button>

      </div>
    );
  }
}

export default App;
