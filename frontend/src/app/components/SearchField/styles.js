import { styled } from '@mui/material/styles';
import { Paper, Button } from '@mui/material';

export const StyledPaper = styled(Paper)(({ theme }) => ({
    padding: theme.spacing(3),
    marginTop: theme.spacing(2),
    marginButton:theme.spacing(2) ,
    backgroundColor: theme.palette.background.paper,
}));

export const StyledButton = styled(Button)(({ theme }) => ({
    marginTop: theme.spacing(2),
}));
