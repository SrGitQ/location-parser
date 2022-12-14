import React from 'react';
import { LBox } from './boxes';
import { Cards } from './organisms';
import { Title } from './text';
import Place from '../utils/types';

type Props = {
	competency: Place[] | null;
}

const Competency: React.FC <Props> = ({competency}) => {
	return (
		<LBox>
            <div className='h-[0.5rem]'></div>
			<Title title='Competency'/>
			<Cards competency={competency}/>
		</LBox>
	);
};

export default Competency;
