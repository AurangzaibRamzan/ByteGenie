import React from 'react';
import { Container, AppBar, Toolbar, Typography } from '@mui/material';

const Layout = ({ children }) => {
  return (
    <Container style={{backgroundColor:'white'}}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">
            ByteGenie AI-Powered Application
          </Typography>
        </Toolbar>
      </AppBar>
      {children}
    </Container>
  );
};

export default Layout;
