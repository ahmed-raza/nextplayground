// src/app/(auth)/signin/page.tsx
import Link from "next/link";

export default function SignInPage() {
  return (
    <>
      <h1 className="mb-6 text-3xl font-bold text-center">Sign In</h1>
      <form className="space-y-4">
        <input
          type="email"
          placeholder="Email"
          className="w-full rounded-md bg-white/10 px-4 py-2 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full rounded-md bg-white/10 px-4 py-2 text-white placeholder-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="submit"
          className="w-full rounded-md bg-blue-600 px-4 py-2 font-semibold hover:bg-blue-700"
        >
          Sign In
        </button>
      </form>
      <p className="mt-4 text-center text-sm text-gray-400">
        Don't have an account?{" "}
        <Link href="/signup" className="text-blue-400 hover:underline">
          Sign up
        </Link>
      </p>
    </>
  );
}
