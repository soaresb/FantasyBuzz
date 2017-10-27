import React from 'react';
import { Button, Form, FormGroup, Label, Input, FormText, Jumbotron, Container } from 'reactstrap';
import BuzzNav from '../Components/BuzzNav';
import Select from 'react-select';
import $ from 'jquery';
var divStyle = {
  width:'80%',
  margin: 'auto',
  backgroundColor: '#f9f9f9'
};
var temp = [];
export default class Example extends React.Component {
  constructor(){
    super();
    this.state = {
      qbs:[],
      rbs:[],
      wrs:[],
      rboptions:[],
      qboptions:[],
      wroptions:[],
      rb1:{"value":"","label":""},
      rb2:{"value":"","label":""},
      qb:{"value":"","label":""},
      wr1:{"value":"","label":""},
      wr2:{"value":"","label":""}
    }
  }

  rb1Change = (val) => {
    console.log("Selected: " + JSON.stringify(val));
    if (val !== null){
      this.setState({rb1:{"value":val.value,"label":val.value}});
    }
  }
  rb2Change = (val) => {
    console.log("Selected: " + JSON.stringify(val));
    if (val !== null){
      this.setState({rb2:{"value":val.value,"label":val.value}});
    }
  }
  qbChange = (val) => {
    console.log("Selected: " + JSON.stringify(val));
    if (val !== null){
      this.setState({qb:{"value":val.value,"label":val.value}});
    }
  }
  wr1Change = (val) => {
    console.log("Selected: " + JSON.stringify(val));
    if (val !== null){
      this.setState({wr1:{"value":val.value,"label":val.value}});
    }
  }
  wr2Change = (val) => {
    console.log("Selected: " + JSON.stringify(val));
    if (val !== null){
      this.setState({wr2:{"value":val.value,"label":val.value}});
    }
  }
  fillQBOptions(){
    if (this.state.qboptions && this.state.qboptions.length >0){

    }
    else{
    for (let player of this.state.qbs){
      this.state.qboptions.push({value: player.name, label:player.name})
    }
  }
  }
  fillRBOptions(){
    if (this.state.rboptions && this.state.rboptions.length >0){

    }
    else{
    for (let player of this.state.rbs){
      this.state.rboptions.push({value: player.name, label:player.name})
    }
  }

  }
  fillWROptions(){
    if (this.state.wroptions && this.state.wroptions.length >0){

    }
    else{
    for (let player of this.state.wrs){
      this.state.wroptions.push({value: player.name, label:player.name})
    }
  }

  }
  getQB(){
    $.ajax({
      url: 'https://lolstats-backend.herokuapp.com/ffb/allQB',
      dataType:'json',
      cache:false,
      success: function(data){
        this.setState({qbs: data});
        if (this.state.qboptions && this.state.qboptions.length > 0){
        }
        else{
          this.fillQBOptions();
        }
      }.bind(this),


      error: function(xhr, status, err){
        console.log(err);
      }
    });
  }
  getRB(){
    $.ajax({
      url: 'https://lolstats-backend.herokuapp.com/ffb/allRB',
      dataType:'json',
      cache:false,
      success: function(data){
        this.setState({rbs: data});
        if (this.state.rboptions && this.state.rboptions.length > 0){
        }
        else{
          this.fillRBOptions();
        }
      }.bind(this),
      error: function(xhr, status, err){
        console.log(err);
      }
    });
  }
  getWR(){
    $.ajax({
      url: 'https://lolstats-backend.herokuapp.com/ffb/allWR',
      dataType:'json',
      cache:false,
      success: function(data){
        this.setState({wrs: data});
        if (this.state.wroptions && this.state.wroptions.length > 0){
        }
        else{
          this.fillWROptions();
        }
      }.bind(this),
      error: function(xhr, status, err){
        console.log(err);
      }
    });
  }
  componentWillMount(){
    this.getQB();
    this.getRB();
    this.getWR();

  }

  componentDidMount(){
    this.getQB();
    this.getRB();
    this.fillRBOptions();
    this.getWR();

  }
  render() {
    return (
      <div>
        <BuzzNav />
        <Jumbotron fluid>
          <Container fluid>
            <h1 className="display-3">Import Team</h1>
            <p className="lead">Import your fantasy team to see the buzz around your players</p>
          </Container>
        </Jumbotron>
        <div style={divStyle}>
          <Form>
            <FormGroup>
              <Label for="exampleSelect">QB</Label>
              <Select
                name="form-field-name"
                value={this.state.qb}
                options={this.state.qboptions}
                onChange={this.qbChange}
              />
              <Label for="exampleSelect">RB</Label>
              <Select
                name="form-field-name"
                value={this.state.rb1}
                options={this.state.rboptions}
                onChange={this.rb1Change}
              />
              <Label for="exampleSelect">RB</Label>
              <Select
                name="form-field-name"
                value={this.state.rb2}
                options={this.state.rboptions}
                onChange={this.rb2Change}
              />
              <Label for="exampleSelect">WR</Label>
              <Select
                name="form-field-name"
                value={this.state.wr1}
                options={this.state.wroptions}
                onChange={this.wr1Change}
              />
              <Label for="exampleSelect">WR</Label>
              <Select
                name="form-field-name"
                value={this.state.wr2}
                options={this.state.wroptions}
                onChange={this.wr2Change}
              />
            </FormGroup>

          </Form>
        </div>


      </div>
    );
  }
}
