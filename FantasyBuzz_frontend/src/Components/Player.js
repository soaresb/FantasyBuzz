import React, { Component } from 'react';
import PlayerItem from "./PlayerItem"

var divStyle = {
  width:'80%',
  margin: 'auto',
  backgroundColor: '#f9f9f9'
};
class Player extends Component {


  render() {
    let players;
    let count=0
    if(this.props.player){
      players = this.props.player.map(player => {
        count = count + 1;
        return(
          <PlayerItem key={player._id.$oid} player={player} num={count}/>
        );

      })
    }
      return(
        <div style={divStyle} >{players}</div>
    );

  }

}


export default Player;
