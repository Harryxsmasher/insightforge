export default function TopNavigation() {

    return (

        <header
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

            <div
                className="
                    mx-auto

                    flex

                    h-20

                    max-w-screen-xl

                    items-center

                    justify-between

                    px-8
                "
            >

                {/* Logo */}

                <div
                    className="
                        flex
                        items-center
                        gap-3
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

                    <h1
                        className="
                            text-xl

                            font-bold

                            text-white
                        "
                    >

                        InsightForge

                    </h1>

                </div>

                {/* Navigation */}

                <nav
                    className="
                        flex

                        items-center

                        gap-10

                        text-sm

                        text-slate-400
                    "
                >

                    <button
                        className="
                            transition-all

                            hover:text-white
                        "
                    >
                        Workspace
                    </button>

                    <button
                        className="
                            transition-all

                            hover:text-white
                        "
                    >
                        About
                    </button>

                    <button
                        className="
                            transition-all

                            hover:text-white
                        "
                    >
                        Settings
                    </button>

                </nav>

            </div>

        </header>

    );

}