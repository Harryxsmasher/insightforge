import { motion } from "framer-motion";

import HeroTitle from "./HeroTitle";
import HeroDescription from "./HeroDescription";

import {
    IFButton,
    IFBadge,
    IFContainer,
    IFSection,
} from "../ui";

import { LuUpload } from "react-icons/lu";

export default function Hero() {

    return (

        <IFSection
            className="
                relative
                overflow-hidden
            "
        >

            {/* Blue Glow */}

            <div
                className="
                    absolute

                    left-1/2
                    top-1/2

                    h-[700px]
                    w-[700px]

                    -translate-x-1/2
                    -translate-y-1/2

                    rounded-full

                    bg-blue-500/10

                    blur-[180px]
                "
            />

            {/* Purple Glow */}

            <div
                className="
                    absolute

                    right-20
                    top-32

                    h-[350px]
                    w-[350px]

                    rounded-full

                    bg-violet-500/10

                    blur-[160px]
                "
            />

            <IFContainer>

                <motion.div

                    initial={{
                        opacity:0,
                        y:40
                    }}

                    animate={{
                        opacity:1,
                        y:0
                    }}

                    transition={{
                        duration:.8
                    }}

                    className="
                        relative
                        z-10

                        flex
                        flex-col

                        items-center

                        text-center
                    "

                >

                    <p
                        className="
                            mb-6

                            uppercase

                            tracking-[0.35em]

                            text-sm

                            text-blue-400
                        "
                    >

                        InsightForge

                    </p>

                    <HeroTitle />

                    <HeroDescription />

                    <IFButton
                        className="
                            mt-12
                        "
                    >

                        <LuUpload size={18}/>

                        Upload Dataset

                    </IFButton>

                    <div
                        className="
                            mt-10

                            flex

                            flex-wrap

                            justify-center

                            gap-3
                        "
                    >

                        <IFBadge>

                            CSV

                        </IFBadge>

                        <IFBadge>

                            Excel

                        </IFBadge>

                        <IFBadge>

                            JSON

                        </IFBadge>

                        <IFBadge
                            variant="success"
                        >

                            AI Powered

                        </IFBadge>

                    </div>

                </motion.div>

            </IFContainer>

        </IFSection>

    );

}