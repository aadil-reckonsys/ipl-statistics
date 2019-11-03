import React from 'react';
import { RouteComponentProps, StaticContext } from "react-router";
import { Form, FormGroup, Label, Input, Container, Row, Col } from "reactstrap";
import MatchDetail from 'components/matchDetails';
import { BASE_URL } from "../../constants";


function IPLYearOptions() {
  let dateList = ['-------']
  for(let i = 2012; i <= new Date().getFullYear(); i++) {
    dateList.push(i.toString())
  }
  return dateList.map(v => (
    <option value={v}>{v}</option>
  ));

}

function GetIPLData(year:any, setState:any) {
  return fetch(`${BASE_URL}/matches/stats/${year}/`)
    .then((data) => data.json())
    .then((data) => setState(data))
    .catch(err => {
      console.log(err);
      setState({});
    });
}

function MainPage(props: RouteComponentProps<any, StaticContext, any>) {
  let [stats, setStats] = React.useState({});
  return (
    <Container>
      <Row>
        <Col>
          <Form>
            <FormGroup>
              <Label for='season'>Select Season</Label>
              <Input type="select" name="year" id="season" onChange={e => GetIPLData(e.target.value, setStats)}>
                {IPLYearOptions()}
              </Input>
            </FormGroup>
          </Form>
        </Col>
      </Row>
      <Row>
        <Col>
          { 
            Object.keys(stats).length ?
              <MatchDetail {...stats} />
              : <p>No Data</p>
          }
        </Col>
      </Row>
    </Container>
  )
}

export default MainPage
