import React, { Component } from 'react';
import '../App.css';
import $ from 'jquery';
import Player from '../Components/Player';
import { FormGroup, Label, Input } from 'reactstrap';
import BuzzNav from '../Components/BuzzNav';
import { browserHistory } from 'react-router';
class DFS_home extends Component {
  constructor(){
    super();
    this.state = {
      players:[],
      value:"ALL",
      url:'https://lolstats-backend.herokuapp.com/ffb/dfs/all'
    }
  }
  change = (event) =>{
    this.setState({value: event.target.value}, () => {
      console.log(this.state.value);
      if (this.state.value==="QB"){
        this.setState({url:'https://lolstats-backend.herokuapp.com/ffb/dfs/QBs'},() => {
          this.getStats();
        })
      }
      if (this.state.value==="RB"){
        this.setState({url:'https://lolstats-backend.herokuapp.com/ffb/dfs/RBs'},() => {
          this.getStats();
        })
      }
      if (this.state.value==="WR"){
        this.setState({url:'https://lolstats-backend.herokuapp.com/ffb/dfs/WRs'},() => {
          this.getStats();
        })
      }
      if (this.state.value==="TE"){
        this.setState({url:'https://lolstats-backend.herokuapp.com/ffb/dfs/TEs'},() => {
          this.getStats();
        })
      }
      if (this.state.value==="ALL"){
        this.setState({url:'https://lolstats-backend.herokuapp.com/ffb/dfs/all'},() => {
          this.getStats();
        })
      }
    });

  }


  getStats(){
    $.ajax({
      url: this.state.url,
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

export default DFS_home;
