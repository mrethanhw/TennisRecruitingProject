import React, { Component } from "react";
import { useTable } from 'react-table'
//import { Col, Container, Row } from "reactstrap";
import PlayerList from "./PlayerList";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    players: []
  };

  componentDidMount() {
    this.resetState();
  }

  getPlayers = () => {
    axios.get(API_URL).then(res => this.setState({ players: res.data }));
  };

  resetState = () => {
    this.getPlayers();
  };

  render() {
    return (
      <div style={{
        padding: '80px',
//
        marginLeft: "12.5%",
        marginRight: '20%'
                  }}>
            <PlayerList
              players={this.state.players}
              resetState={this.resetState}
            />
        </div>
        /* <Row>
          <Col>
            <NewStudentModal create={true} resetState={this.resetState} />
          </Col>
        </Row> */
      //</Container>
    );
  }
}

export default Home;