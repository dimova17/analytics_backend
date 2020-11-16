import {createStyles, Theme} from "@material-ui/core";

export default (theme: Theme) => createStyles({
    button: {
        color: theme.palette.secondary.main
    },
    // @ts-ignore
    popper: {
        // @ts-ignore
        zIndex: '10000 !important',
    },
    menuPaper: {
        boxShadow: '0px 0px 20px -2px rgba(160, 159, 159, 0.42)'
    },
});