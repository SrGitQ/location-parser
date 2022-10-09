import React from 'react';

type Props = {
    title: string;
}

const Rating: React.FC<Props> = ({title}) => {
    return (
        <div className='text-5xl text-center'>
            {title}
        </div>
    );
}

export default Rating;