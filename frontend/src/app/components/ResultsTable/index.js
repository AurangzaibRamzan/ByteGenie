import React from 'react';
import { TableBody, TableCell } from '@mui/material';
import { 
  StyledTableContainer, 
  StyledTable, 
  StyledTableHead, 
  StyledTableHeadCell, 
  StyledTableRow } from './styles';

const ResultsTable = ({ results }) => (
  <StyledTableContainer>
    <StyledTable>
      <StyledTableHead>
        <StyledTableRow>
          {Object.keys(results[0]).map((key) => (
            <StyledTableHeadCell key={key}>{key}</StyledTableHeadCell>
          ))}
        </StyledTableRow>
      </StyledTableHead>
      <TableBody>
        {results.map((row, rowIndex) => (
          <StyledTableRow key={rowIndex}>
            {Object.keys(row).map((key, colIndex) => (
              <TableCell key={`${rowIndex}-${colIndex}`}>
                {row[key]}
              </TableCell>
            ))}
          </StyledTableRow>
        ))}
      </TableBody>
    </StyledTable>
  </StyledTableContainer>
);

export default ResultsTable;
