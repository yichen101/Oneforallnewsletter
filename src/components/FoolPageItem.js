import classes from "./FoolPageItem.module.css"

function FoolPageItem(props) {
    return (
        <div>
            {Object.keys(props.items).map((item, index) => { //Loop into each item
                return (
                <div className={classes.card}>
                    <a href={props.items[item].link} className={classes.title}>
                        {props.items[item].title}
                    </a>
                    <p>
                        {props.items[item].teaser}
                    </p>
                </div>
                )
            })}
        </div>
    )
}
export default FoolPageItem