import React from 'react';
import { BasicInformation, Metrics, Charts, Competency } from './components';
import Place from './utils/types';

type Props = {
  place: Place | null;
};

const Layout: React.FC <Props> = ({place}) => {
    return place ? (
        
      <div className="grid-rows-4">
        <BasicInformation place={place}/>
        <Metrics wordCloud={place.wordCloud} sentiment={place.sentiment} visitorData={place.visitorData}/>
        <Charts busyDays={place.busyDays} busyHours={place.busyHours}/>
        <Competency competency={place.competency}/>
        <div className='text-orange-700'>{1+3}</div>
      </div>
    ) : (<></>)
}

export default Layout;
