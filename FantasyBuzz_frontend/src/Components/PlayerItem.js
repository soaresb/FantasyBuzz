import React, { Component } from 'react';
import { Media } from 'reactstrap';


var divStyle = {
  textAlign:'left'
};
class PlayerItem extends Component {

  render() {

    return (

      <Media>
        <Media left href="#">
          <Media object src={this.props.player.url} style={{width: 130, height: 130}} />
        </Media>
        <Media body>
          <Media heading style={divStyle}>
            {this.props.player.name}
          </Media>
          {this.props.player.value}
        </Media>
    </Media>
    );
  }
}




export default PlayerItem;
