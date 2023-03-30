import React, { useEffect, useState }  from 'react'
import { FaAngleDoubleUp } from 'react-icons/fa'
import classes from './ScrollToTop.module.css'

function ScrollToTop() {
    const [showScrollTopButton, setShowScrollTopButton] = useState(false)

    useEffect(() => {
        window.addEventListener("scroll", () => {
            if (window.scrollY>300) {
                setShowScrollTopButton(true)
            }
            else {
                setShowScrollTopButton(false)
            }
        });
    }, [])

    const scrollTop = () => {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    };
    return (
        <div>
            {showScrollTopButton && <FaAngleDoubleUp onClick={scrollTop} className={classes.topButton}/>}
        </div>
    )
}

export default ScrollToTop