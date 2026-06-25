import { motion } from "framer-motion";

import HeroTitle from "./HeroTitle";
import HeroDescription from "./HeroDescription";
import HeroButton from "./HeroButton";

export default function Hero() {
    return (
        <section
            className="
                relative
                flex
                items-center
                justify-center

                min-h-[calc(100vh-80px)]

                overflow-hidden

                px-6
            "
        >
            {/* Background Glow */}
            <div
                className="
                    absolute

                    h-[700px]
                    w-[700px]

                    rounded-full

                    bg-blue-500/10

                    blur-[180px]
                "
            />

            {/* Hero Content */}
            <motion.div
                className="
                    relative
                    z-10

                    flex
                    flex-col
                    items-center

                    text-center

                    max-w-5xl
                "
                initial={{
                    opacity: 0,
                    y: 40,
                }}
                animate={{
                    opacity: 1,
                    y: 0,
                }}
                transition={{
                    duration: 0.8,
                }}
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

                <HeroButton />
            </motion.div>
        </section>
    );
}