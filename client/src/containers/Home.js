import React from 'react';

import Navbar from '../components/Navbar';

export default class Home extends React.Component {
render() {
    return (
    <React.Fragment>
    <Navbar/>
      <p1 styles={{justifyContent: 'center', alignItems: 'center'}}>
        Improve your social skills!
      </p1>
    </React.Fragment>
      );
    }
  }