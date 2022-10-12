import React from 'react';

type Props = {
    title: string;
}

const GText: React.FC<Props> = ({title}) => {
    return (
        <div className='text-3xl text-center'>
            {title}
        </div>
    );
}

export default GText;
