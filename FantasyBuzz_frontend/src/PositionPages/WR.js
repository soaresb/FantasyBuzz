import React, { Component } from 'react';
import '../App.css';
import $ from 'jquery';
import Player from '../Components/Player';
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
        <div></div>
        <Player player={this.state.players} />



      </div>
    );
  }
}

export default WR;
