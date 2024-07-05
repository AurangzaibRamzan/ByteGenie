import { styled } from '@mui/material/styles';
import { Table, TableHead, TableCell, TableRow } from '@mui/material';

export const StyledTableContainer = styled('div')(({ theme }) => ({
    marginTop: theme.spacing(3),
    overflowX: 'auto',
}));

export const StyledTable = styled(Table)(({ theme }) => ({
    minWidth: 650,
}));

export const StyledTableHead = styled(TableHead)(({ theme }) => ({
    backgroundColor: theme.palette.primary.light,
}));

export const StyledTableHeadCell = styled(TableCell)(({ theme }) => ({
    color: theme.palette.primary.contrastText,
    fontWeight: 'bold',
}));

export const StyledTableRow = styled(TableRow)(({ theme }) => ({
    '&:nth-of-type(odd)': {
        backgroundColor: theme.palette.action.hover,
    },
}));
