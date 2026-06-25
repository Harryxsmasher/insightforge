import type { PropsWithChildren } from "react";

import TopNavigation from "./TopNavigation";

export default function WorkspaceLayout({

    children,

}: PropsWithChildren) {

    return (

        <div
            className="
                min-h-screen

                bg-[#09090B]

                text-white
            "
        >

            <TopNavigation />

            <main>

                {children}

            </main>

        </div>

    );

}