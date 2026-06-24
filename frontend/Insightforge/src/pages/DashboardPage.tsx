import Sidebar from "../components/Sidebar"


export default function DashboardPage() {

    return (

        <div
            style={{
                display: "flex"
            }}
        >

            <Sidebar />

            <div
                style={{
                    padding: "20px"
                }}
            >

                <h1>Dashboard</h1>

                <p>

                    Welcome to InsightForge

                </p>

            </div>

        </div>

    )

}