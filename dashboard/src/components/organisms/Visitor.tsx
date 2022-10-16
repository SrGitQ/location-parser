import React from 'react';
import { Bullet } from '../text';


type Props = {
    website: string;
    id: string;
}

const Visitor: React.FC <Props> = ({website, id}) => {
    return (
		<div className='h-56 rounded-lg flex'>
            <div className='h-56 rounded-l-lg bg-zinc-200 w-3/4 p-6 grid content-center'>
                <p className='text-center text-neutral-400 text-lg'>Visit the website of this place on...<br/><a href={website}>{website}</a></p>
            </div>
            <div className='h-56 rounded-r-lg bg-zinc-100 w-2/4 p-8 grid content-center'>
                <img className='m-auto' src={'http://localhost:5000/static/codes/'+id+'_QR.png'} width='150px' alt='QR CODE'/>
            </div>
        </div>
    );
};

export default Visitor;
