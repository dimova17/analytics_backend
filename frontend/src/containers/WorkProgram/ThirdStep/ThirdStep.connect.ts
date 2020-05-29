import {Dispatch} from "react";
import {connect} from 'react-redux';
import {bindActionCreators} from "redux";

import actions from "../actions";
import {getWorkProgramField} from '../getters';
import {fields} from "../enum";
import {WorkProgramActions} from "../types";

import {rootState} from "../../../store/reducers";

const mapStateToProps = (state:rootState) => {
    return {
        sections: getWorkProgramField(state, fields.WORK_PROGRAM_SECTIONS),
    };
};

const mapDispatchToProps = (dispatch: Dispatch<WorkProgramActions>) => ({
    // @ts-ignore
    actions: bindActionCreators(actions, dispatch),
});

// @ts-ignore
export default connect(mapStateToProps, mapDispatchToProps);