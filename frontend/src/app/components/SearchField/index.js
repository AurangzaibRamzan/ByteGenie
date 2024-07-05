import React from 'react';
import { TextField } from '@mui/material';
import { StyledPaper, StyledButton } from './styles';

const SearchField = ({ query, setQuery, handleSearch }) => (
  <StyledPaper>
    <TextField
      label="Enter your query"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      fullWidth
      variant="outlined"
      margin="normal"
    />
    <StyledButton variant="contained" color="primary" onClick={handleSearch}>
      Search
    </StyledButton>
  </StyledPaper>
);

export default SearchField;
