import classes from "./FoolPageList.module.css"
import FoolPageItem from "./FoolPageItem"

function FoolPageList(props) {
  return (
    <div>
      {Object.keys(props.pages).map((page, i) => { //Loop into each page
        return (
            <div className={classes.box} key={props.sections[i].id} id={props.sections[i].id}>
              <h1 className={classes.textCenter}>
                {page//Display page name
                }
              </h1>
              <FoolPageItem items={props.pages[page]}/>
            </div>
          )
      })}
    </div>
     )

}
export default FoolPageList