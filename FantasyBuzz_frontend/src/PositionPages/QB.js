import React, { Component } from 'react';
import '../App.css';
import $ from 'jquery';
import Player from '../Components/Player';

import BuzzNav from '../Components/BuzzNav'
class QB extends Component {
  constructor(){
    super();
    this.state = {
      players:[]
    }
  }
  getStats(){
    $.ajax({
      url: 'https://lolstats-backend.herokuapp.com/ffb/QBs',
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
        

        <Player player={this.state.players} />



      </div>
    );
  }
}

export default QB;
