import { motion } from "framer-motion";

import { IFContainer } from "../components/ui";

export default function TopNavigation() {
    return (
        <motion.header
            initial={{ y: -30, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.6 }}
            className="
                sticky
                top-0
                z-50

                border-b
                border-white/10

                bg-black/20

                backdrop-blur-xl
            "
        >
            <IFContainer>
                <div
                    className="
                        flex
                        h-20
                        items-center
                        justify-between
                    "
                >
                    {/* Logo */}

                    <div
                        className="
                            flex
                            items-center
                            gap-3
                            cursor-pointer
                            select-none
                        "
                    >
                        <div
                            className="
                                h-3
                                w-3
                                rounded-full

                                bg-blue-500

                                shadow-lg
                                shadow-blue-500/60
                            "
                        />

                        <div className="flex flex-col">
                            <span
                                className="
                                    text-lg
                                    font-bold
                                    tracking-tight
                                    text-white
                                "
                            >
                                InsightForge
                            </span>

                            <span
                                className="
                                    text-xs
                                    text-slate-500
                                "
                            >
                                AI Data Intelligence
                            </span>
                        </div>
                    </div>

                    {/* Navigation */}

                    <nav
                        className="
                            flex
                            items-center
                            gap-10
                        "
                    >
                        <button
                            className="
                                relative

                                text-sm
                                text-slate-400

                                transition-colors
                                duration-300

                                hover:text-white
                            "
                        >
                            Workspace
                        </button>

                        <button
                            className="
                                text-sm
                                text-slate-400

                                transition-colors
                                duration-300

                                hover:text-white
                            "
                        >
                            About
                        </button>

                        <button
                            className="
                                text-sm
                                text-slate-400

                                transition-colors
                                duration-300

                                hover:text-white
                            "
                        >
                            Settings
                        </button>
                    </nav>
                </div>
            </IFContainer>
        </motion.header>
    );
}