import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { regular } from '@fortawesome/fontawesome-svg-core/import.macro'
import { Title } from '../text';
import { RBox } from '../boxes';

type Props = {
    qal: Array<number>;
}

const HeadsUp: React.FC <Props> = ({qal}) => {
	return (

		<RBox>
            <Title title='People think'/>
		    <div className='mt-6 grid grid-cols-3'>
		    	<div className='flex justify-center'>
		    		<div className='text-center'>
		    			<FontAwesomeIcon icon={regular('face-frown')} className='text-red-600 text-7xl'/>
		    			<div className='text-neutral-400'>{qal[0]}%</div>
		    		</div>
		    	</div>
		    	<div className='flex justify-center'>
		    		<div className='text-center'>
		    			<FontAwesomeIcon icon={regular('face-meh')} className='text-amber-400 text-7xl'/>
		    			<div className='text-neutral-400'>{qal[1]}%</div>
		    		</div>
		    	</div>
		    	<div className='flex justify-center'>
		    		<div className='text-center'>
		    			<FontAwesomeIcon icon={regular('face-smile')} className='text-green-600 text-7xl'/>
		    			<div className='text-neutral-400'>{qal[2]}%</div>
		    		</div>
		    	</div>
		    </div>
        </RBox>
	);
}
export default HeadsUp;