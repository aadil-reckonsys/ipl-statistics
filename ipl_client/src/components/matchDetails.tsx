import React from "react";
import { ListGroup, ListGroupItem, ListGroupItemHeading, ListGroupItemText } from 'reactstrap';

function SnakeToHuman(value:string) {
  value = value.split('_').join(' ')
  value = value[0].toUpperCase() + value.slice(1)
  return value
}

function GetListData(props:any) {
  let items = [];
  for(let key in props) {
    if (props.hasOwnProperty(key)) {
      items.push(<ListGroupItemHeading>{SnakeToHuman(key)}</ListGroupItemHeading>);
      if(Array.isArray(props[key])) {
        props[key].forEach((item:any) => items.push(<ListGroupItemText>{item}</ListGroupItemText>));
      }
      else {
        items.push(<ListGroupItemText>{props[key]}</ListGroupItemText>)
      }
    }
  }
  return items;
}

function MatchDetail(props:any) {
  return (
    <div>
      <ListGroup>
        <ListGroupItem className="details">
          {GetListData(props)}
        </ListGroupItem>
      </ListGroup>
    </div>
  )
}

export default MatchDetail;
