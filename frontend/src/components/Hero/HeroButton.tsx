import { LuUpload } from "react-icons/lu";

export default function HeroButton() {
    return (
        <button
            className="
                mt-12

                inline-flex
                items-center
                gap-3

                rounded-2xl

                border
                border-blue-500/30

                bg-blue-500/10

                px-8
                py-4

                text-white
                font-medium

                backdrop-blur-md

                transition-all
                duration-300

                hover:bg-blue-500/20
                hover:border-blue-400
                hover:scale-105
            "
        >
            <LuUpload size={20} />

            Upload Dataset
        </button>
    );
}