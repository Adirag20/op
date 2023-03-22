import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: process.env.LARAVEL_SAIL
      ? Object.values(os.networkInterfaces())
          .flat()
          .find((info) => info?.internal === false)?.address
      : undefined,
  },
});
