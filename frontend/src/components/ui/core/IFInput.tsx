import type { InputHTMLAttributes } from "react";

type IFInputProps = InputHTMLAttributes<HTMLInputElement>;

export default function IFInput(props: IFInputProps) {
    return (
        <input
            className="
                w-full

                rounded-2xl

                border
                border-white/10

                bg-white/5

                px-5
                py-4

                text-white

                placeholder:text-slate-500

                outline-none

                transition

                focus:border-blue-500
            "
            {...props}
        />
    );
}