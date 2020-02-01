import React from 'react';

import PropTypes from 'prop-types';

import './Layout.css';

const propTypes = {
  children: PropTypes.node.isRequired,
  contentCenter: PropTypes.bool
};

const defaultProps = {
  contentCenter: false
};

const Layout = ({ children, contentCenter }) => {
  return (
    <section>
      <header>
        <h1>Social Lite</h1>
      </header>
      <main className={contentCenter ? 'content-center' : ''}>{children}</main>
      <footer>
        <p>
         An application to help you live life.
        </p>
      </footer>
    </section>
  );
};

Layout.propTypes = propTypes;
Layout.defaultProps = defaultProps;

export default Layout;
