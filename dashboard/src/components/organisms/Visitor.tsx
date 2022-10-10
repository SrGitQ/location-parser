import React from 'react';
import { Bullet } from '../text';

type VisitorData = {
	url: string;
}

type Props = {
    visitorData: VisitorData;
}

const Visitor: React.FC <Props> = ({visitorData}) => {
    return (
		<div className='h-56 rounded-lg flex'>
            <div className='h-56 rounded-l-lg bg-zinc-200 w-3/4 p-6 grid content-center'>
                <p className='text-center'><Bullet>Visit the website of this place on...<br/>{visitorData.url}</Bullet></p>
            </div>
            <div className='h-56 rounded-r-lg bg-zinc-100 w-2/4 p-8 grid content-center'>
                <img className='m-auto' src='https://www.vippng.com/png/full/380-3801625_aplicaciones-eventbee-qr-code-design-png.png' width='150px' alt='QR CODE'/>
            </div>
        </div>
    );
};

export default Visitor;
