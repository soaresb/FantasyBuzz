import React, { Component } from 'react';
import '../App.css';
import $ from 'jquery';
import Player from '../Components/Player';
import { Button } from 'reactstrap';
import BuzzNav from '../Components/BuzzNav'
class WR extends Component {
  constructor(){
    super();
    this.state = {
      players:[]
    }
  }
  getStats(){
    $.ajax({
      url: 'https://lolstats-backend.herokuapp.com/ffb/WRs',
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
        <header className="App-header">
          <h1 className="App-title">FantasyBuzz</h1>
          <hr color="white"/>
          <BuzzNav />
        </header>

        <Player player={this.state.players} />

        <Button color="danger">Danger!</Button>

      </div>
    );
  }
}

export default WR;
