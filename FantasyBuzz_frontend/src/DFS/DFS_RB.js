import React, { Component } from 'react';
import '../App.css';
import $ from 'jquery';
import Player from '../Components/Player';
import { FormGroup, Label, Input } from 'reactstrap';
import BuzzNav from '../Components/BuzzNav';
import { browserHistory } from 'react-router';
class DFS_RB extends Component {
  constructor(){
    super();
    this.state = {
      players:[],
      value:"RB",

    }
  }
  change = (event) =>{
    this.setState({value: event.target.value}, () => {
      console.log(this.state.value);
      browserHistory.push(this.state.value);
    });

  }


  getStats(){
    $.ajax({
      url: 'https://lolstats-backend.herokuapp.com/ffb/dfs/RBs',
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
        <FormGroup>
          <Label for="exampleSelect">Select</Label>
          <Input type="select" name="select" id="exampleSelect" onChange={this.change} value={this.state.value}>
            <option>ALL</option>
            <option>QB</option>
            <option>RB</option>
            <option>WR</option>
            <option>TE</option>

          </Input>
        </FormGroup>
        <Player player={this.state.players} />



      </div>
    );
  }
}

export default DFS_RB;
